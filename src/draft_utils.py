import os
import json

def ensure_drafts_file(drafts_file: str) -> str:
    """
    Ensure the drafts file exists following these rules:

    - If the provided drafts_file does not exist and it is a simple filename (i.e., it does not contain
      any path separator), then use the XDG Base Directory Specification to determine a cache directory:
        * It checks for the XDG_CACHE_HOME environment variable.
        * If not set, defaults to HOME/.cache.
      Then, a sub-folder named "threads-cli" is created within that cache directory, and
      drafts_file is placed inside that sub-folder.
      
    - If drafts_file is a simple filename, but a file does not exist at that location, or if it is given as a full 
      path, the application uses that path exactly as given.
      
    - If the drafts file does not exist, create an empty JSON file (with an empty dict as content by default).

    Returns:
        The final path to the drafts file.
    
    Raises:
        EnvironmentError: If the required HOME environment variable is not set when needed.
    """
    # Check if drafts_file doesn't exist and is a simple filename (without path separator).
    if not os.path.exists(drafts_file) and os.path.sep not in drafts_file:
        # Determine the cache directory using XDG_CACHE_HOME if available,
        # otherwise default to HOME/.cache.
        xdg_cache_home = os.getenv('XDG_CACHE_HOME')
        if not xdg_cache_home:
            home = os.getenv('HOME')
            if not home:
                raise EnvironmentError("HOME environment variable is not set.")
            xdg_cache_home = os.path.join(home, '.cache')
        # Define the final path: XDG_CACHE_HOME/threads-cli/drafts_file
        drafts_dir = os.path.join(xdg_cache_home, "threads-cli")
        os.makedirs(drafts_dir, exist_ok=True)
        drafts_file = os.path.join(drafts_dir, drafts_file)

    # If the drafts file still does not exist, create an empty JSON file.
    if not os.path.exists(drafts_file):
        with open(drafts_file, "w") as f:
            json.dump({}, f)
    
    return drafts_file
