# RHEL-RPM-Build-Sample
Red Hat Linux RPM Build Sample from library files (no source code)

This repository contains a sample for building an RPM package from library files yourself on Redhat linux. Tested on RHEL 7.3 and also 6.8 with a slight modification.

As a sample, we try to build an RPM of OpenCV, Tesseract and Leptonica.

## Procedure
First install the required tools

```bash
sudo yum group install -y 'Development Tools'

# Some important packages
sudo yum install -y cmake git unzip wget

# First install the required development packages for opencv
sudo yum install -y libjpeg-devel libtiff-devel libpng-devel zlib-devel gtk2-devel pkgconfig \
        dialog openssl-devel ncurses-devel texinfo qt-devel tcl-devel tk-devel kernel-headers kernel-devel
```

### Compile OpenCV

```bash
# Clone, build opencv and install opencv
cd ~ && \
git clone  https://github.com/opencv/opencv.git && \
cd opencv && mkdir release && cd release && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .. && make -j16 && sudo make install
```

### Compile Leptonica

```bash
# Download, build and install leptonica
cd ~ && \
wget http://www.leptonica.org/source/leptonica-1.74.1.tar.gz && \
tar -zxvf leptonica-1.74.1.tar.gz && \
cd leptonica-1.74.1 && \
./configure && \
make -j 32 && sudo make install
```

### Compile tesseract
```bash
# Clone, build and install tesseract
cd ~ && \
git clone https://github.com/shahrukhqasim/tesseract.git && \
cd tesseract && \
./autogen.sh && \
./configure && \
LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make -j 32 && \
sudo make install && \
sudo ldconfig
```

### Building RPM
Now finally, we get on to building the RPM ourselves. First we have to create a directory structure similar to how it works when libraries are installed. And then copy all the required files from system to over here. And package them in an archive:
```bash
# Time to build RPM package for the three libraries above
cd ~ && \
mkdir -p libs_combined-1 && \
cd libs_combined-1 && \
mkdir -p usr/local/libs/ && \
cd usr/local/libs/ && \
cp /usr/local/lib/libopencv* . && \
cp /usr/local/lib/libtess* . && \
cp /usr/local/lib/liblept* . && \
cd ~ && \
tar -zcvf libs_combined-1.tar.gz libs_combined-1/
```

After this, we have to create a directory structure like this
```bash
cd ~ && \
mkdir -p rpmbuild && \
cd rpmbuild && \
mkdir -p BUILD RPMS SOURCES SPECS SRPMS && \
cd SPECS
```

Now create a file `spec1.spec` here from the sample given in this repository. When done, run these commands
```bash
cd ~ && \
cp libs_combined-1.tar.gz rpmbuild/SOURCES/ && \
cd rpmbuild/SPECS/ && \
rpmbuild -ba spec-1.spec
```

### Achivement
RPM should be present in ~/rpmbuild/RPMS/<architecture>/
