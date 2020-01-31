from msmrw.guide import Guide

try:
    from guidesencoder.config import DevConfig
except ImportError:
    import sys
    sys.path.append('.')
    from guidesencoder.config import DevConfig

if __name__ == "__main__":
    guide = Guide("Python Guide")
    guide.get()
    guide.createGuideFile()
    # guide.encodeGuideFile()
