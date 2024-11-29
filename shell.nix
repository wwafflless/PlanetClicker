{ pkgs ? import <nixpkgs> { } }:

with pkgs;

mkShell {
  buildInputs = with pkgs;[
    uv
    python312
    python312Packages.numpy
    python312Packages.pygame
    python312Packages.tkinter
    python312Packages.pygame-ce
    python312Packages.pygame-gui
    python312Packages.toml
  ];
  shellHook = ''
    export SDL_VIDEODRIVER=wayland
  '';
}
