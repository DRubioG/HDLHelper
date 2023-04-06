library IEEE;
use IEEE.std_logic_1164.all;

entity Decoder_tb is
end entity Decoder_tb;

architecture arch_Decoder_tb of Decoder_tb is

component Decoder_tb is
	generic (
		Y   	 : integer;
		U   	 : integer          := 	32;
		N, T	 : integer;
		GAD 	 : std_logic_vector := 	N-1
	);
	port (
		CLK, rst 	 : in  	std_logic;
		Row      	 : in  	std_logic_vector((N-1) downto (N-2));
		Col      	 : out 	std_logic_vector(3 downto 0);
		DecodeOut	 : out 	std_logic_vector(3 downto 0));
end component;

constant Y  	 : integer;
constant U  	 : integer := 	32;
constant N, T 	 : integer;
constant GAD	 : std_logic_vector := 	N-1;

signal CLK_i, rst_i : std_logic;
signal Row_i       : std_logic_vector((N-1) downto (N-2));
signal Col_i       : std_logic_vector(3 downto 0);
signal DecodeOut_i : std_logic_vector(3 downto 0);

begin

Decoder_inst : Decoder_tb
	generic map (
		Y  	 => 	Y,
		U  	 => 	U,
		N  	 => 	N,
		T  	 => 	T,
		GAD	 => 	GAD,
	)
	port map (
		CLK        => 	CLK_i,
		rst        => 	rst_i,
		Row        => 	R_i,
		Col        => 	C_i,
		DecodeOut  => 	D_i
	);
end architecture arch_Decoder_tb;