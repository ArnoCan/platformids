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

import com.sun.jna.Native;
import com.sun.jna.platform.win32.WinNT;
import com.sun.jna.ptr.IntByReference;

import java.util.Map;
//import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

/**
 * @author Arno-Can Uestuensoez <acue_sf2 @ sourceforge.net>
 * @version 0.1.1
 * @since 0.1.30
 *
 *
 *        Read product information of the WindowsNT family by JNA. Requires the
 *        structure *OSVERSIONINFOEXA*, thus the interface *GetVersionExA* which
 *        is not available by *com.sun.jna.platform.win32.Kernel32*, thus uses
 *        direct calls of *Kernel32*.
 *
 */
public class Kernel32GetProductInfo {

	public interface Kernel32 extends com.sun.jna.platform.win32.Kernel32 {
		Kernel32 INSTANCE = (Kernel32) Native.loadLibrary("kernel32", Kernel32.class,
				com.sun.jna.win32.W32APIOptions.DEFAULT_OPTIONS);

		boolean GetProductInfo(int dwOSMajorVersion, int dwOSMinorVersion, int dwSpMajorVersion, int dwSpMinorVersion,
				IntByReference pdwReturnedProductType);

		boolean GetVersionEx(WinNT.OSVERSIONINFOEX lpVersionInfo);

	}

	/**
	 * Get product type, return by ref pointer.
	 *
	 * @param major
	 *            Major OS version.
	 * @param minor
	 *            Minor OS version.
	 * @param smajor
	 *            Major SP version.
	 * @param sminor
	 *            Minor SP version.
	 * @param typeLst
	 *            Value by reference for the product type, Jython requires a
	 *            List.
	 * @return boolean
	 */
	public boolean GetProductInfo(int major, int minor, int smajor, int sminor, List typeLst) {
		IntByReference myref = new IntByReference();
		boolean res = Kernel32GetProductInfo.Kernel32.INSTANCE.GetProductInfo(major, minor, smajor, sminor, myref);
		typeLst.set(0, myref.getValue());
		return res;
	}

	/**
	 * Get product type, return by ref pointer.
	 *
	 * @param versx
	 *            Value by reference for the product version Map.
	 * @return boolean
	 */
	// public boolean GetVersionEx(Map<String, String> versx) {
	// public boolean GetVersionEx(Map versx) {
	public boolean GetVersionEx(Map<String, Object> versx) {
		WinNT.OSVERSIONINFOEX _vx = new WinNT.OSVERSIONINFOEX();
		boolean res = Kernel32GetProductInfo.Kernel32.INSTANCE.GetVersionEx(_vx);

		// versx["build"] = _vx.dwBuildNumber;
		versx.put("dwOSVersionInfoSize", _vx.dwOSVersionInfoSize);
		versx.put(" dwMajorVersion", _vx.dwMajorVersion);
		versx.put(" dwMinorVersion", _vx.dwMinorVersion);
		versx.put("dwBuildNumber", _vx.dwBuildNumber);
		versx.put("dwBuildNumber", _vx.dwBuildNumber);
		versx.put("dwPlatformId", _vx.dwPlatformId);
		versx.put("szCSDVersion", _vx.szCSDVersion);
		versx.put("wServicePackMajor", _vx.wServicePackMajor);
		versx.put("wServicePackMinor", _vx.wServicePackMinor);
		versx.put("wSuiteMask", _vx.wSuiteMask);
		versx.put("wReserved", _vx.wReserved);
		versx.put("wProductType", _vx.wProductType);

		return res;
	}

}
