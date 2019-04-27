#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-analogue
Version  : 0.17.1
Release  : 19
URL      : https://cran.r-project.org/src/contrib/analogue_0.17-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/analogue_0.17-1.tar.gz
Summary  : Analogue and Weighted Averaging Methods for Palaeoecology
Group    : Development/Tools
License  : GPL-2.0
Requires: R-analogue-lib = %{version}-%{release}
BuildRequires : R-brglm
BuildRequires : R-princurve
BuildRequires : R-vegan
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
# analogue
#### Released version
[![CRAN version](http://www.r-pkg.org/badges/version/analogue)](https://cran.r-project.org/package=analogue) [![](http://cranlogs.r-pkg.org/badges/grand-total/analogue)](https://cran.r-project.org/package=analogue)

%package lib
Summary: lib components for the R-analogue package.
Group: Libraries

%description lib
lib components for the R-analogue package.


%prep
%setup -q -c -n analogue

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552711082

%install
export SOURCE_DATE_EPOCH=1552711082
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library analogue
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library analogue
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library analogue
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  analogue || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/analogue/CITATION
/usr/lib64/R/library/analogue/COPYING
/usr/lib64/R/library/analogue/ChangeLog
/usr/lib64/R/library/analogue/DESCRIPTION
/usr/lib64/R/library/analogue/INDEX
/usr/lib64/R/library/analogue/Meta/Rd.rds
/usr/lib64/R/library/analogue/Meta/data.rds
/usr/lib64/R/library/analogue/Meta/features.rds
/usr/lib64/R/library/analogue/Meta/hsearch.rds
/usr/lib64/R/library/analogue/Meta/links.rds
/usr/lib64/R/library/analogue/Meta/nsInfo.rds
/usr/lib64/R/library/analogue/Meta/package.rds
/usr/lib64/R/library/analogue/Meta/vignette.rds
/usr/lib64/R/library/analogue/NAMESPACE
/usr/lib64/R/library/analogue/NEWS
/usr/lib64/R/library/analogue/ONEWS.Rd
/usr/lib64/R/library/analogue/R/analogue
/usr/lib64/R/library/analogue/R/analogue.rdb
/usr/lib64/R/library/analogue/R/analogue.rdx
/usr/lib64/R/library/analogue/THANKS
/usr/lib64/R/library/analogue/TODO
/usr/lib64/R/library/analogue/data/Biome.rda
/usr/lib64/R/library/analogue/data/Climate.rda
/usr/lib64/R/library/analogue/data/ImbrieKipp.rda
/usr/lib64/R/library/analogue/data/Location.rda
/usr/lib64/R/library/analogue/data/Pollen.rda
/usr/lib64/R/library/analogue/data/Salinity.rda
/usr/lib64/R/library/analogue/data/SumSST.rda
/usr/lib64/R/library/analogue/data/V12.122.rda
/usr/lib64/R/library/analogue/data/WinSST.rda
/usr/lib64/R/library/analogue/data/abernethy.rda
/usr/lib64/R/library/analogue/data/rlgh.rda
/usr/lib64/R/library/analogue/data/swapdiat.rda
/usr/lib64/R/library/analogue/data/swappH.rda
/usr/lib64/R/library/analogue/doc/analogue_methods.R
/usr/lib64/R/library/analogue/doc/analogue_methods.Rnw
/usr/lib64/R/library/analogue/doc/analogue_methods.pdf
/usr/lib64/R/library/analogue/doc/index.html
/usr/lib64/R/library/analogue/help/AnIndex
/usr/lib64/R/library/analogue/help/aliases.rds
/usr/lib64/R/library/analogue/help/analogue.rdb
/usr/lib64/R/library/analogue/help/analogue.rdx
/usr/lib64/R/library/analogue/help/paths.rds
/usr/lib64/R/library/analogue/html/00Index.html
/usr/lib64/R/library/analogue/html/R.css
/usr/lib64/R/library/analogue/tests/Examples/analogue-Ex.Rout.save
/usr/lib64/R/library/analogue/tests/test-all.R
/usr/lib64/R/library/analogue/tests/testthat/test-analog.R
/usr/lib64/R/library/analogue/tests/testthat/test-new-distance.R
/usr/lib64/R/library/analogue/tests/testthat/test-tran.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/analogue/libs/analogue.so
/usr/lib64/R/library/analogue/libs/analogue.so.avx2
/usr/lib64/R/library/analogue/libs/analogue.so.avx512
