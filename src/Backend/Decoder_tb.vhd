library IEEE;
use IEEE.std_logic_1164.all;

component Decoder is
	generic (
        n, 	t,  : integer 32;
        g : std_logic n-1;
	)	
    port ( 
        clk, rst : 	in s (t d _);	--alfa
        row         : 	in      std_logic_vector (n-1 downto 0);	--dfhdfg
        col         : 	out     std_logic_vector (3 downto 0);	--dfhdfg1
        decodeout   : 	out     std_logic_vector (3 downto 0)
    );
end component;
