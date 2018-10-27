# Image to text python script

Simple script that converts given image to text file.
Made bacause I learned about numpy.digitize function, that simplified whole proccess a lot.

### What you need to install to run this script
You only need to have '''pipenv''' installed.

# Usage:
### What to do first
- clone/download this repository
- open it in console/terminal
- type '''pipenv install''' and press enter (wait for installations to finish)
- type '''pipenv shell''' and press enter
Now you are ready to run this script.
### Example of usage:
'python image_to_txt.py python-logo.png <width> <height> (not neccessary)'
You can customize results by changing 'SMALL_SPECTRUM' in 'result = image_to_ascii(image_file, width, height, SMALL_SPECTRUM)' 
image_to_text.py to one of 'INVERSED_SPECTRUM FULL_SPECTRUM SMALL_SPECTRUM'

Result:
'''python
                       -----------------+                       
                   --------------------------                   
                 ------=-----------------------                 
                :----     ----------------------                
                :----     ----------------------                
                :-------------------------------                
                --------------------------------                
                                ----------------                
       -----------------------------------------  ********      
    --------------------------------------------  ***********   
  ----------------------------------------------  ************  
 -----------------------------------------------  ************* 
 ----------------------------------------------  %**************
-----------------------------------------------  ***************
---------------------------------------------   ****************
--------------------------------:--==+=        *****************
------------------        %*************************************
----------------   *********************************************
---------------   **********************************************
 --------------  ********************************************** 
 --------------  ********************************************** 
  ------------- %*********************************************  
   -----------: %*******************************************    
      --------= %****************************************       
                %***************                                
                %*******************************                
                %*******************************                
                %*********************     *****                
                 *********************      ****                
                 ******************************                 
                   **************************%                  
                       ******************%                      
'''
