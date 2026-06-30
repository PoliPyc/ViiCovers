# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['app/main.py'],
    pathex=['/home/runner/work/ViiCovers/ViiCovers'],
    binaries=[],
    datas=[('./data/*', 'data')],  # Kopiuje zawartość folderu data do folderu data w dist
    hiddenimports=['PIL._tkinter_finder', 'FreeSimpleGUI', 'PIL'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ViiCovers',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Zmienione na False, aby ukryć konsolę dla zwykłego użytkownika
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ViiCovers',
)