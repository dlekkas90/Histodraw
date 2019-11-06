#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:40:38 2019

@author: dlekkas
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from glob import glob
from math import sqrt

print '\n', ' P R O G R A M  I N I T I A L I Z E D . . .', '\n'*2

print '+------------------------------- HISTODRAW  v1.0 --------------------------+' 
print '|                                                                          |'
print '|   LINE DRAWER AND AUTOMATIC DISTANCE CALCULATOR FOR HISTOLOGICAL IMAGES  |' 
print '|                                                                          |'
print '|             [ Conceived and Coded by Damien Lekkas (c) 2019 ]            |'
print '|                                                                          |'
print '+--------------------------------------------------------------------------+', '\n'


read_dir = './VWF/input_images/*'
input_files = []

for f in glob(read_dir):
    input_files.append(f)

histodraw_data_out = open('histodraw_data_out.txt', 'a+')

plt.ion()

threshold = input(' > SET THE DESIRED THRESHOLD LENGTH (IN PIXELS) FOR LINE FILTERING: ')
histodraw_data_out.write('THRESHOLD LENGTH = ' + str(threshold) + '\n'*2)

  
for f in input_files:
    drawn_lines = 0
    accepted_lines = 0  
    
    histodraw_data_out.write('\n' + f.split('/')[-1].split('.')[0] + '\n')
    histodraw_data_out.write('--------------------------' + '\n')
    another_flag = 'y'
    
    while another_flag != 'n':
       
        img = mpimg.imread(f)
        imgplot = plt.imshow(img)
        plt.show(block=False)
        imgplot = plt.imshow(img)
        
        point1 = raw_input(' > SPECIFY X,Y COORDINATES FOR LINE ORIGIN: ')
        plt.scatter([int(point1.split(',')[0])],[int(point1.split(',')[1])], c='y', s=15)
    
        imgplot = plt.imshow(img)
        plt.show(block=False)
    
        point2 = raw_input(' > SPECIFY X,Y COORDINATES FOR LINE END POINT: ')
        plt.scatter([int(point1.split(',')[0])],[int(point1.split(',')[1])], c='y', s=15)
        plt.scatter([int(point2.split(',')[0])],[int(point2.split(',')[1])], c='y', s=15)
    
        imgplot = plt.imshow(img)
    
        plt.plot([int(point1.split(',')[0]), int(point2.split(',')[0])], [int(point1.split(',')[1]), int(point2.split(',')[1])], 'y-') 
        imgplot = plt.imshow(img)
        plt.show(block=False)
    
        line_length = sqrt(abs(int(point2.split(',')[0]) - int(point1.split(',')[0]))**2 + abs(int(point2.split(',')[1]) - int(point1.split(',')[1]))**2)  
        drawn_lines += 1
        print '\n' + ' > LENGTH OF LINE DRAWN IS ', round(line_length,2), ' PIXELS'
        
        histodraw_data_out.write(str(round(line_length,2)) + '\n')
    
        if round(line_length,2) < threshold:
            accepted_lines += 1
    
        another_flag = raw_input(' > DRAW ANOTHER LINE (y/n)? ')

    histodraw_data_out.write('ACCEPTED LINES: ' + str(accepted_lines) + ' / ' + str(drawn_lines) + '\n'*2)

    if input_files[-1] != f:
        raw_input(' > PRESS ENTER TO CONTINUE TO NEXT IMAGE ')

    else:
        print '\n', ' > ALL IMAGES IN THE INPUT DIRECTORY HAVE BEEN PROCESSED!', '\n'
        raw_input(' > PRESS ENTER TO EXIT PROGRAM ') 

    plt.clf()
    
histodraw_data_out.close() 

print '\n'*2, 'P R O G R A M  T E R M I N A T E D', '\n' 
