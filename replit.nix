{ pkgs }: {
  deps = [
		pkgs.python39Packages.pip
  pkgs.2
  pkgs.python39Packages.pip
  pkgs.python39Packages.bootstrapped-pip
  pkgs.python39Packages.bootstrapped-pip
  pkgs.python39Packages.bootstrapped-pip
  pkgs.python38Packages.pip
  pkgs.python39Packages.pip
  pkgs.import os
  pkgs.nodePackages.prettier
    pkgs.python38Full
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}