{
  description = "PlanetClicker flake";

  inputs.nixpkgs.url = "nixpkgs/nixos-24.05";
  inputs.pyproject-nix.url = "github:nix-community/pyproject.nix";
  inputs.pyproject-nix.inputs.nixpkgs.follows = "nixpkgs";

  outputs = { nixpkgs, pyproject-nix, ... }:
    let
      inherit (nixpkgs) lib;

      project = pyproject-nix.lib.project.loadPyproject {
        projectRoot = ./.;
      };

      pkgs = import nixpkgs {
        system = "x86_64-linux";
      };
      python = pkgs.python3;

    in
    {
      devShells.x86_64-linux.default =
        let
          arg = project.renderers.withPackages { inherit python; };
          pythonEnv = python.withPackages arg;
        in
        pkgs.mkShell {
          packages = [ pythonEnv ];
        };

      packages.x86_64-linux.default =
        let
          attrs = project.renderers.buildPythonPackage { inherit python; };
        in
        python.pkgs.buildPythonPackage attrs;
    };
}
