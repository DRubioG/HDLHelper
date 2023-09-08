-----------------------------------------------
-- Created using HDLHelper 0.0
-- Create Date: 2023-09-08 12:05:49.393396
-----------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;

entity Decoder_tb is
end entity Decoder_tb;

architecture arch_Decoder_tb of Decoder_tb is

component Decoder_tb is
	generic (
		YFG6YUGIUKJ	 : 	integer;            	   	-- hola 2
		U          	 : 	integer          := 	32;	-- hola
		N, T       	 : 	integer;            	   	-- prueba
		GAD        	 : 	std_logic_vector := 	N-1	-- preuba3
	);
	port (
		clk, rst, yhmm       	 : in  	std_logic;                           		-- alfa
		Rowerererrererererere	 : in  	std_logic_vector((N-1) downto (N-2));		-- dfhdfg
		Col                  	 : out 	std_logic_vector(3 downto 0);        		-- dfhdfg1
		DecodeOut            	 : out 	std_logic_vector(3 downto 0));       		-- marcafa
end component;

constant YFG6YUGIUKJ : integer;
constant U           : integer	 := 32;
constant N           : integer;
constant T           : integer;
constant GAD         : std_logic_vector	 := N-1;

signal clk_i                   : std_logic;
signal rst_i                   : std_logic;
signal yhmm_i                  : std_logic;
signal Rowerererrererererere_i : std_logic_vector((N-1) downto (N-2));
signal Col_i                   : std_logic_vector(3 downto 0);
signal DecodeOut_i             : std_logic_vector(3 downto 0);


begin

Decoder_inst : Decoder_tb
	generic map (
		YFG6YUGIUKJ	 => 	YFG6YUGIUKJ,
		U          	 => 	U,
		N          	 => 	N,
		T          	 => 	T,
		GAD        	 => 	GAD
	)
	port map (
		clk                  	 => 	clk_i,
		rst                  	 => 	rst_i,
		yhmm                 	 => 	yhmm_i,
		Rowerererrererererere	 => 	Rowerererrererererere_i,
		Col                  	 => 	Col_i,
		DecodeOut            	 => 	DecodeOut_i,
	);

	clk <= not(clk) after 5 ns;
	rst <= '0', '1' after 20 ns;

end architecture arch_Decoder_tb;