
clc
clear all
close all


N = 65;
w = window( @triang , N );%blue
w1 = window( @hamming , N );%green
w2 = window( @gausswin , N , 2.5 );%red
wvtool( w , w1 , w2 );


group_number=3;
f1 = group_number * 33;
f2 = group_number * 42;
frequency = 1024;
n1 = 100;
n2 = 1000;

t1 = ( 0 : n1 - 1 ) / frequency;
t2 = ( 0 : n2 - 1 ) / frequency;
y1 = sin( 2 * pi * f1 * t1 ) + sin( 2 * pi * f2 * t1 );
y2 = sin( 2 * pi * f1 * t2 ) + sin( 2 * pi * f2 * t2 );

figure( 2 );
subplot( 2 , 1 , 1 ); 
plot( t1 , y1 );
xlabel( 'time' );
ylabel( 'amp' );
title( 'y1' );
grid on
subplot( 2 , 1 , 2 ); 
plot( t2 , y2 );
xlabel( 'time' );
ylabel( 'amp' );
title( 'y2' );
grid on


N1 = 64;                   
N2 = 1024;                  
F1_1 = abs( fft( y1 , N1 ) );
F1_2 = abs( fft( y1 , N2 ) );
F2_1 = abs( fft( y2 , N1 ) );
F2_2 = abs( fft( y2 , N2 ) );

coefficientsFourier = [ F1_1 , F1_2 , F2_1 , F2_2 ];
LengthsCoefficientsFourier = [ length( F1_1 ) , length( F1_2 ), length( F2_1 ) , length( F2_2 ) ];

figure( 3 );
ind = 0;
for i = 1:4
    disp( ind );
    Nfft = coefficientsFourier( ind + 1 : ind + LengthsCoefficientsFourier( i ));
    ind = ind + LengthsCoefficientsFourier( i );
    Nfft = Nfft( 1 : length( Nfft ) / 2 );
    subplot( 4 , 1 , i );
    plot( Nfft );
    xlabel( 'frequency' );
    ylabel( 'power' );
    grid on
end
