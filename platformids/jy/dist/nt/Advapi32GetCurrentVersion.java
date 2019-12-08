/**
 *
 * Requires in classpath:
 *
 *  jna.jar
 *  jna-platform.jar
 *  win32-x86-64.jar / win32-x86.jar 
 *
 * see: https://github.com/java-native-access/jna/tree/master/dist
 *
 */

package platformids.dist.nt;

import java.util.TreeMap;
import com.sun.jna.platform.win32.Advapi32;
import com.sun.jna.platform.win32.WinReg.HKEY;
import com.sun.jna.platform.win32.WinReg.HKEYByReference;
import com.sun.jna.platform.win32.WinNT;
import com.sun.jna.platform.win32.W32Errors;
import com.sun.jna.platform.win32.Win32Exception;
import com.sun.jna.platform.win32.Advapi32Util;

import static com.sun.jna.platform.win32.WinReg.HKEY_LOCAL_MACHINE;

/**
 * @author Arno-Can Uestuensoez <acue_sf2 @ sourceforge.net>
 * @version 0.1.1
 * @since 0.1.30
 */
public class Advapi32GetCurrentVersion {

	/**
	 * Get attribute names and values of registry key.
	 *
	 * @param root
	 *            Root key.
	 * @param keyPath
	 *            Path to a registry key.
	 * @return TreMap<String, Object> of registry name value pairs.
	 */
	public static TreeMap<String, Object> registryGetValues(HKEY root, String keyPath) {
		HKEYByReference phkKey = new HKEYByReference();
		int rc = Advapi32.INSTANCE.RegOpenKeyEx(root, keyPath, 0, WinNT.KEY_READ, phkKey);
		if (rc != W32Errors.ERROR_SUCCESS) {
			throw new Win32Exception(rc);
		}
		try {
			vals =Advapi32Util.registryGetValues(phkKey.getValue());
		} finally {
			rc = Advapi32.INSTANCE.RegCloseKey(phkKey.getValue());
			if (rc != W32Errors.ERROR_SUCCESS) {
				throw new Win32Exception(rc);
			}
		}
		return vals;

	}

	/**
	 * Get key-value pairs of the registry key's attributes:
	 *
	 * "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion"
	 *
	 * @return Map of of registry names and values for CurrentVersion.
	 */
	public static TreeMap<String, Object> getCurrentVersionValues() {
		return registryGetValues(HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion");
	}

}
