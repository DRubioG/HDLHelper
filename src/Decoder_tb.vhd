-----------------------------------------------
-- Created using HDLHelper 0.0
-- Create Date: 2023-09-06 20:00:34.146766
-----------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;

entity Decoder_tb is
end entity Decoder_tb;

architecture arch_Decoder_tb of Decoder_tb is

component Decoder_tb is
	generic (
		YFG6YUGIUKJ	 : integer;
		U          	 : integer          := 	32;
		N, T       	 : integer;
		GAD        	 : std_logic_vector := 	N-1
	);
	port (
		clk, rst, yhmm       	 : in  	std_logic;
		Rowerererrererererere	 : in  	std_logic_vector((N-1) downto (N-2));
		Col                  	 : out 	std_logic_vector(3 downto 0);
		DecodeOut            	 : out 	std_logic_vector(3 downto 0));
end component;

constant YFG6YUGIUKJ	 : integer;
constant U          	 : integer := 	32;
constant N, T         	 : integer;
constant GAD        	 : std_logic_vector := 	N-1;

signal a_clk_i, a_rst_i, a_yhmm_i : std_logic;
signal a_Rowerererrererererere_i  : std_logic_vector((N-1) downto (N-2));
signal a_Col_i                    : std_logic_vector(3 downto 0);
signal a_DecodeOut_i              : std_logic_vector(3 downto 0);

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
		clk                    => 	a_clk_i,
		rst                    => 	a_rst_i,
		yhmm                   => 	a_yhmm_i,
		Rowerererrererererere  => 	a_R_i,
		Col                    => 	a_C_i,
		DecodeOut              => 	a_D_i
	);

	clk <= not(clk) after 5 ns;
	rst <= '0', '1' after 20 ns;

end architecture arch_Decoder_tb;