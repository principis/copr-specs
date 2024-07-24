
## If OPENCV_LOG_LEVEL is not set, set to ERROR otherwise it would default to INFO.
[ -z "$OPENCV_LOG_LEVEL" ] && OPENCV_LOG_LEVEL="ERROR" && export OPENCV_LOG_LEVEL

## Uncomment the following line to disable Intel MFX messages
#[ -z "$OPENCV_VIDEOIO_PRIORITY_INTEL_MFX" ] && OPENCV_VIDEOIO_PRIORITY_INTEL_MFX=0 && export OPENCV_VIDEOIO_PRIORITY_INTEL_MFX
