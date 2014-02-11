//
//  arching_an_arrow.c
//  arching_an_arrow
//
//  Created by Raichu on 2/6/14.
//  Copyright (c) 2014 richard. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "arching_an_arrow.h"
#include "input_utilities.h"

unsigned int range 					=	0;
unsigned int enemy_distance =	0;

void instructions ( void )
{
    printf ( "Arching An Arrow\n" );
    printf ( "Created by Richard on 5/13/13.\n" );
    printf ( "\n" );
    
    boolean show_instructions = get_yes_no ( "Would you like instructions? " );
    
    if ( show_instructions )
    {
        printf	(	"\n"
                 "This game allows you to adjust the "
                 "angle of your bow to fire at "
                 "a stationary target. Hitting within "
                 "2 yards of the target is a confirmed "
                 "hit. Specify the number of degrees "
                 "of elevation of your bow: 45 degrees "
                 "provides maximum range with values "
                 "under or over 45 degrees providing "
                 "less range."
                 "\n\n"
                 );
    }
}

void intialization ( void )
{
    // setting max range
    const unsigned int min_firing_distance	= 35;
    
    range = 70; //( ( rand() % min_range ) + min_firing_distance );
    
    printf ( "Your bow shoots up to %d yards away.\n", range );
    
    // enemy distance
    enemy_distance = ( int )( ( rand() % ( range - min_firing_distance ) ) + min_firing_distance  );
    
    printf ( "Your target is %d yards away\n", enemy_distance );
}

void event_loop ( void )
{
    boolean keep_playing	= false;
    boolean enemy_dead		= false;
    unsigned int ammo 		= 0;
    
    do
    {
        // initialize
        
        // NEEDS TO BE ADDED
        /*
         printf ( "\n"
         "You are the officer-in-charge, giving order to the crew "
         "telling them the degrees of elevation you estimate will "
         "place a projectile within 100 yards of the enemy."
         "\n\n" );
         */
        
        intialization();
        
        // game phase
        enemy_dead	= false;
        ammo		= 5;
        
        do
        {
          printf ( "What angle do you want to shoot your bow at? Arrows: %d\n", ammo );
          
          unsigned int angle = get_int_range ( 1, 89 );
          
          float angle_to_radians = 2 * angle / 57.3;
          
          int	distance_fired = range * sin ( angle_to_radians );
          
          printf ( "You shot %d yards", distance_fired );
          
          int distance_from_taget = enemy_distance - distance_fired;
          
          if ( distance_from_taget <= 2 && distance_from_taget >= -2 )
          {
              if (distance_from_taget == 0)
              {
                printf ( ". Great shot, bullseye!\n" );
              }
              else
              {
                printf ( ". You hit the target, well done!\n" );
              }
              
              enemy_dead = true;
          }
          else if ( distance_from_taget > distance_fired )
          {
              printf ( ", your shot feel short.\n" );
          }
          else
          {
              printf ( ", your shot went over the target.\n" );
          }
          
          ammo--;
          
          if (ammo == 0)
          {
              printf("You're out of arrows.\n");
              
              enemy_dead = true;
          }
          
        }
        while ( enemy_dead == false );
        
        // play again
        keep_playing = get_yes_no ( "Would you like to play again? " );
    }
    while ( keep_playing );
}

void terminate ( void )
{
  printf ( "\nHope you enjoyed the fun, come again!\n" );
}






