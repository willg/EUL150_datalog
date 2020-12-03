with (import <nixpkgs> {});
let
    pythonEnv = python3.withPackages (ps: [
        ps.pyserial
   ]);
in mkShell {
    buildInputs = [
        pythonEnv
    ];
}
