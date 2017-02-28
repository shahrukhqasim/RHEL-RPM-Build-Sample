%undefine _missing_build_ids_terminate_build

Name:		libs_combined
Version:	1
Release:	1%{?dist}
Summary:	Contains OpenCV, Tesseract and Leptonica

Group:		1
License:	Edit
URL:		github.com
Source0:	libs_combined-1.tar.gz

BuildRequires:	gcc

%description


%prep
%setup -q

%build



%install
cp * -r %{buildroot}


%files
/*

%doc



%changelog

