About this fork
===========

Modifying py-expander to be able to add Google Drive uploading along side existing Amazon Drive Upload Capability
by utilizing PyDrive's wrappers and utilizing an authentication-less form of access by way of ServiceLevelAuthentication
to prevent script from interruption.

It may be possible to call a 'sync' command similar to the way ACD allows access, but to my knowlege this isn't possible.

Using Google Drive in this way requires the creation of a Service Level Account to be created within the Developers Console
and copying the resulting authentication keyfile that is created upon creating the account to where transmission is running
locally.  

Unfortunately this requires the use a couple of additional libraries that I'll make to sure to list as I move forward.



py-expander
===========

A python script designed to post-process Transmission torrents.

The script extracts files recursively (if extract is necessary)
and the moves the files to pre-configured directories based on their type.
If no RARs are present in the download - the script will copy the files.

The script relies on the 'guessit' package to detect movies/tv downloads.

Original torrent files are conserved for upload.

The script can also fetch subtitles in chosen languages (change in the config file),  
and upload the videos to an Amazon cloud storage account.

All original torrent names are kept the original names log file.

Currently only 7-Zip is supported. (Make sure to use the version with the rar plugin, or compile from source with 'make all')

Usage
===========
Install the script as follows:

	$ python setup.py develop

Edit the configuration with your directories

	$ vim config.py

That's it.

The script can be used from the command line:

	$ pyexpand /download/The.Wire.S01E01.HDTV

For transmission:

	$ vim /var/lib/transmission/settings.json
	..
	 "script-torrent-done-enabled": true,
     "script-torrent-done-filename": "pyexpand",
    ..

Or for uTorrent:

    Options -> Advanced -> Run Program
    When download is finished, run (Change paths accordingly): 
	'C:\Python35\pythonw.exe D:\Projects\py-expander\src\pyexpander\torrent_handler.py "%D" "%F"'
	
	Important: Be sure to use different directories for new downloads and completed downloads, or else pyexpander won't work.

* Make sure that the transmission user can run `pyexpand`. If not:

	$ ln -s /usr/local/bin/pyexpand /usr/bin/pyexpand
