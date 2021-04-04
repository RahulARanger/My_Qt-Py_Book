# QRC

## Uses?

Used when we need to access the resources files from any Path

## How to use it?

* Write a qrc file (follows XML format) containing the paths of all files (relative to the current qrc file/ python path)
    * while writing the qrc file follow this [sample]("https://github.com/RahulARanger/My_PyQt5_Book/tree/master/Handling%20Resources/QRC/note.qrc")
    * Alias and prefix makes us easy to access the data/ resources

* Run the `pyrcc5 -o dest_file_path.py contained_file_path.qrc` command 

* Import that python file 

* use the path `:/prefix_name/alias_name` or `:/prefix_name/file_name_with_extension`
  
* More Reference for above step: [sample]("https://github.com/RahulARanger/My_PyQt5_Book/tree/master/Handling%20Resources/QRC/all_in_one.py")


## Alternative

Refer `pathlib` module, note it is just access the raw media files that is their approaches are different


## Advantages

* we don't need to depend on the path of the resource files

* #### we can delete qrc file and other resource files since everything is copied into the destined python file


## Note:

### Don't try to compress/ use qrc with video or audio files (not recommended)