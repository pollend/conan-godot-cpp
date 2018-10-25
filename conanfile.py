from conans import ConanFile, tools, Scons
import os
from glob import glob


class godoConan(ConanFile):
    name = "eigen"
    version = "3.3.5"
    url = "https://github.com/pollend/conan-godot-cpp"
    homepage = "https://godotengine.org/"
    description = "C++ bindings for the Godot script API"
    no_copy_source = True

    @property
    def source_subfolder(self):
        return "sources"

    def source(self):
        self.run("git clone https://github.com/GodotNativeTools/godot-cpp.git")
        self.run("git submodule update --init --recursive")

    def package(self):
        scons = Scons(self)
        scons.configure(source_folder=self.source_subfolder)
        scons.install()
        self.copy("COPYING.*", dst="licenses", src=self.source_subfolder,
                  ignore_case=True, keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['godot_headers']