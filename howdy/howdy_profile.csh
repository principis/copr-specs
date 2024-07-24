
## If OPENCV_LOG_LEVEL is not set, set to ERROR otherwise it would default to INFO.
if ( ! $?OPENCV_LOG_LEVEL ) setenv OPENCV_LOG_LEVEL ERROR

## Uncomment the following line to disable Intel MFX messages
#if ( ! $?OPENCV_VIDEOIO_PRIORITY_INTEL_MFX ) setenv OPENCV_VIDEOIO_PRIORITY_INTEL_MFX 0
