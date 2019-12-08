/*
 * Read registry by using the interface *java.util.prefs.WindowsPreferences*.
 * 
 * see Stackoverflow.com - Read/write to Windows registry using Java - [SOVFLJAVAREG]_
 *    https://stackoverflow.com/questions/62289/read-write-to-windows-registry-using-java
 *
 * REMARK: 
 *    in case of the warning:
 *
 *       WARNING: Could not open/create prefs root node Software\JavaSoft\Prefs at root 0x80000002. Windows RegCreateKeyEx(...) returned error code 5.
 *
 *    create the key manually:
 *
 *        HKEY_LOCAL_MACHINE\Software\JavaSoft\Prefs
 *
 */

package platformids.dist.nt;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.prefs.Preferences;


public class ReadCurrentVersionWinPrefs {

	public static final int HKEY_CURRENT_USER = 0x80000001, HKEY_LOCAL_MACHINE = 0x80000002, REG_SUCCESS = 0,
			REG_NOTFOUND = 2, REG_ACCESSDENIED = 5, KEY_ALL_ACCESS = 0xf003f, KEY_READ = 0x20019;
	private static final Preferences userRoot = Preferences.userRoot(), systemRoot = Preferences.systemRoot();
	private static final Class<? extends Preferences> userClass = userRoot.getClass();
	private static Method regOpenKey, regCloseKey, regQueryValueEx, regEnumValue, regQueryInfoKey, regEnumKeyEx;

	static {
		/*
		 * define imports from WindowsPreferences
		 */
		try {
			(regOpenKey = userClass.getDeclaredMethod("WindowsRegOpenKey",
					new Class[] { int.class, byte[].class, int.class })).setAccessible(true);
			(regCloseKey = userClass.getDeclaredMethod("WindowsRegCloseKey", new Class[] { int.class }))
					.setAccessible(true);
			(regQueryValueEx = userClass.getDeclaredMethod("WindowsRegQueryValueEx",
					new Class[] { int.class, byte[].class })).setAccessible(true);
			(regEnumValue = userClass.getDeclaredMethod("WindowsRegEnumValue",
					new Class[] { int.class, int.class, int.class })).setAccessible(true);
			(regQueryInfoKey = userClass.getDeclaredMethod("WindowsRegQueryInfoKey1", new Class[] { int.class }))
					.setAccessible(true);
			(regEnumKeyEx = userClass.getDeclaredMethod("WindowsRegEnumKeyEx",
					new Class[] { int.class, int.class, int.class })).setAccessible(true);
		} catch (NoSuchMethodException | SecurityException ex) {
			Logger.getLogger(ReadCurrentVersionWinPrefs.class.getName()).log(Level.SEVERE, null, ex);
		}
	}

	/**
	 * Read a value from key and value name
	 *
	 * @param hkey
	 *            HKEY_CURRENT_USER/HKEY_LOCAL_MACHINE
	 * @param key
	 * @param valueName
	 * @return the value
	 * @throws IllegalArgumentException
	 * @throws IllegalAccessException
	 * @throws InvocationTargetException
	 */
	public static String readString(int hkey, String key, String valueName)
			throws IllegalArgumentException, IllegalAccessException, InvocationTargetException {

		switch (hkey) {
		case HKEY_LOCAL_MACHINE:
			return readString(systemRoot, hkey, key, valueName);
		case HKEY_CURRENT_USER:
			return readString(userRoot, hkey, key, valueName);
		default:
			throw new IllegalArgumentException("hkey=" + hkey);
		}
	}

	/**
	 * Read value(s) and value name(s) form given key
	 *
	 * @param hkey
	 *            HKEY_CURRENT_USER/HKEY_LOCAL_MACHINE
	 * @param key
	 * @return the value name(s) plus the value(s)
	 * @throws IllegalArgumentException
	 * @throws IllegalAccessException
	 * @throws InvocationTargetException
	 */
	public static Map<String, String> readStringValues(int hkey, String key)
			throws IllegalArgumentException, IllegalAccessException, InvocationTargetException {

		switch (hkey) {
		case HKEY_LOCAL_MACHINE:
			return readStringValues(systemRoot, hkey, key);
		case HKEY_CURRENT_USER:
			return readStringValues(userRoot, hkey, key);
		default:
			throw new IllegalArgumentException("hkey=" + hkey);
		}
	}

	/**
	 * Read the value name(s) from a given key
	 *
	 * @param hkey
	 *            HKEY_CURRENT_USER/HKEY_LOCAL_MACHINE
	 * @param key
	 * @return the value name(s)
	 * @throws IllegalArgumentException
	 * @throws IllegalAccessException
	 * @throws InvocationTargetException
	 */
	public static List<String> readStringSubKeys(int hkey, String key)
			throws IllegalArgumentException, IllegalAccessException, InvocationTargetException {

		switch (hkey) {
		case HKEY_LOCAL_MACHINE:
			return readStringSubKeys(systemRoot, hkey, key);
		default:
			throw new IllegalArgumentException("hkey=" + hkey);
		}
	}

	private static String readString(Preferences root, int hkey, String key, String value)
			throws IllegalArgumentException, IllegalAccessException, InvocationTargetException {

		int[] handles = (int[]) regOpenKey.invoke(root, new Object[] { hkey, toCstr(key), KEY_READ });
		if (handles[1] != REG_SUCCESS) {
			return null;
		}
		byte[] valb = (byte[]) regQueryValueEx.invoke(root, new Object[] { handles[0], toCstr(value) });
		regCloseKey.invoke(root, new Object[] { handles[0] });
		return (valb != null ? new String(valb).trim() : null);
	}

	private static Map<String, String> readStringValues(Preferences root, int hkey, String key)
			throws IllegalArgumentException, IllegalAccessException, InvocationTargetException {

		HashMap<String, String> results = new HashMap<>();
		int[] handles = (int[]) regOpenKey.invoke(root, new Object[] { hkey, toCstr(key), KEY_READ });
		if (handles[1] != REG_SUCCESS) {
			return null;
		}
		int[] info = (int[]) regQueryInfoKey.invoke(root, new Object[] { handles[0] });

		int count = info[0]; // Count
		int maxlen = info[3]; // Max value length
		for (int index = 0; index < count; index++) {

			byte[] name = (byte[]) regEnumValue.invoke(root, new Object[] { handles[0], index, maxlen + 1 });

			if (name != null) {
				String value = readString(hkey, key, new String(name));

				System.out.println("index = " + index + " name = " + new String(name) + " value = " + value);

				results.put(new String(name).trim(), value);
			}
		}
		regCloseKey.invoke(root, new Object[] { handles[0] });
		return results;
	}

	private static List<String> readStringSubKeys(Preferences root, int hkey, String key)
			throws IllegalArgumentException, IllegalAccessException, InvocationTargetException {

		List<String> results = new ArrayList<>();
		int[] handles = (int[]) regOpenKey.invoke(root, new Object[] { hkey, toCstr(key), KEY_READ });
		if (handles[1] != REG_SUCCESS) {
			return null;
		}
		int[] info = (int[]) regQueryInfoKey.invoke(root, new Object[] { handles[0] });

		int count = info[0];// Count
		int maxlen = info[3]; // Max value length
		for (int index = 0; index < count; index++) {
			byte[] name = (byte[]) regEnumKeyEx.invoke(root, new Object[] { handles[0], index, maxlen + 1 });
			results.add(new String(name).trim());
		}
		regCloseKey.invoke(root, new Object[] { handles[0] });
		return results;
	}

	private static byte[] toCstr(String str) {

		byte[] result = new byte[str.length() + 1];
		for (int i = 0; i < str.length(); i++) {
			result[i] = (byte) str.charAt(i);
		}
		result[str.length()] = 0;
		return result;
	}
}
