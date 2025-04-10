{
  description = "LLMSP";

  outputs =
    {
      self,
      nixpkgs,
    }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
    in
    {
      devShells.x86_64-linux.default = pkgs.mkShell {
        shellHook = ''
          export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${
            with pkgs;
            lib.makeLibraryPath [
              xorg.libX11
              xorg.libXt
              xorg.libSM
              zlib
              glib
              udev
              libGL
              glfw
              boost
              gmp
            ]
          }:${pkgs.stdenv.cc.cc.lib}/lib"
            source .venv/bin/activate
            export PYTHONPATH="$PYTHONPATH:$VIRTUAL_ENV/lib/python3.11/site-packages"
        '';
        name = "LLMSP";
        buildInputs = with pkgs; [
          python311Packages.pip
          python311Packages.tkinter
          python311Packages.cmake
          python311Packages.openai
          cmake
          gcc
          stdenv
          udev
          libGL
          glfw
          graphviz
          gmp
          #glibc.static
        ];
      };
    };
}
