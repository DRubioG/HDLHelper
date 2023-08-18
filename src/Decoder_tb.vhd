-----------------------------------------------
-- Created using HDLHelper v0.0
-- Designer: 
-----------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;

entity Decoder_tb is
end entity Decoder_tb;

architecture arch_Decoder_tb of Decoder_tb is

component Decoder_tb is
	generic (
		yfg6yugiukj	 : integer;
		U          	 : integer          := 	32;
		N, T       	 : integer;
		Gad        	 : std_logic_vector := 	N-1
	);
	port (
		clk, rst, yhmm       	 : in  	std_logic;
		Rowerererrererererere	 : in  	std_logic_vector((N-1) downto (N-2));
		Col                  	 : out 	std_logic_vector(3 downto 0);
		DecodeOut            	 : out 	std_logic_vector(3 downto 0));
end component;

constant yfg6yugiukj	 : integer;
constant U          	 : integer := 	32;
constant N, T         	 : integer;
constant Gad        	 : std_logic_vector := 	N-1;

signal clk_i, rst_i, yhmm_i  : std_logic;
signal Rowerererrererererere_i : std_logic_vector((N-1) downto (N-2));
signal Col_i                 : std_logic_vector(3 downto 0);
signal DecodeOut_i           : std_logic_vector(3 downto 0);

begin

Decoder_inst : Decoder_tb
	generic map (
		yfg6yugiukj	 => 	yfg6yugiukj,
		U          	 => 	U,
		N          	 => 	N,
		T          	 => 	T,
		Gad        	 => 	Gad,
	)
	port map (
		clk                    => 	clk_i,
		rst                    => 	rst_i,
		yhmm                   => 	yhmm_i,
		Rowerererrererererere  => 	R_i,
		Col                    => 	C_i,
		DecodeOut              => 	D_i
	);

	clk <= not(clk) after 5 ns;
	rst <= '0', '1' after 20 ns;

end architecture arch_Decoder_tb;