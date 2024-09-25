{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.docker-compose
    pkgs.git
    pkgs.openssl
    pkgs.postgresql_12
    pkgs.python311
    pkgs.uv
  ];

  shellHook = ''
    set -a; source .env; set +a
  '';
}
