library IEEE;
use IEEE.std_logic_1164.all;
component Decoder is
	generic (
		Y       	 : integer;            	   		-- hola 2
		U       	 : integer          := 	32;		-- hola
		N, T    	 : integer;            	   		-- prueba
		GADGVSED	 : std_logic_vector := 	N-1		-- preuba3
	)
	port (
		clk, rst 	 : in 	std_logic;                     		-- alfa
		row      	 : in 	std_logic_vector(N-1 downto 0);		-- dfhdfg
		col      	 : out	std_logic_vector(3 downto 0);  		-- dfhdfg1
		decodeout	 : out	std_logic_vector(3 downto 0)); 		-- marcafa
end component;
