group_number  = 65;
window_blackman = window(@blackmanharris,group_number);
window_hamming = window(@hamming,group_number);
plot(1:group_number,[window_blackman,window_hamming])
axis([1 group_number 0 1])