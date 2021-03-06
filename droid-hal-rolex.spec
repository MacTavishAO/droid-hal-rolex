# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device rolex
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 4A

%define droid_target_aarch64 1

%define installable_zip 1

%define straggler_files \
/bugreports\
/d\
/file_contexts.bin\
/init.qcom.sh\
/init.qcom.usb.sh\
/property_contexts\
/sdcard\
/selinux_version\
/service_contexts\
/vendor\
%{nil}

# Fixes WebBrowser crashes
%define android_config \
#define WANT_ADRENO_QUIRKS 1 \
%{nil}

# Add user to media_rw for access to android_storage
%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

