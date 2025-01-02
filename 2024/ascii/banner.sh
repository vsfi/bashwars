#!/bin/bash

echo -e "\n##############################################################"
echo -e   "#                                                            #"
echo -e   "#                 What a beautiful pictures!                 #"
echo -e   "#            But how can we see them in terminal?            #"
echo -e   "#            ascii-image-converter could help us!            #"
echo -e   "#           Usage: ascii-image-converter image.png           #"
echo -e   "#     Wait! seems like this image contains another images!   #"
echo -e   "#   You should cut out all hidden images with size 114 x 128 #"
echo -e   "#                   And read them in order                   #"
echo -e   "#     hint: U can use binwalk for observing hidden images    #"
echo -e   "#                                                            #"
echo -e   "##############################################################"
if [[ $(whoami) != "vsfi" ]]; then
    bash
fi