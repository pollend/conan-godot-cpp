from conans import ConanFile, tools,CMake
import os
from glob import glob


class GodotConan(ConanFile):
    name = "godot"
    version = "3.3.5"
    url = "https://github.com/pollend/conan-godot-cpp"
    homepage = "https://godotengine.org/"
    description = "C++ bindings for the Godot script API"
    no_copy_source = True
    generators = "scons"

    @property
    def source_subfolder(self):
        return "godot-cpp"

    def build(self):
        os.makedirs("build")
        with tools.chdir("build"):
            self.run('scons -C "{}/godot-cpp/"'.format(self.source_folder))

    def source(self):
        self.run("git clone https://github.com/GodotNativeTools/godot-cpp.git")
        self.run("cd godot-cpp && git submodule update --init --recursive")

    def package(self):
        self.copy("*.h", "include", src="src")
        self.copy("*.lib", "lib", keep_path=False)
        self.copy("*.a", "lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['godot_headers']