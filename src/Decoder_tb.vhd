library IEEE;
use IEEE.std_logic_1164.all;

entity Decoder_tb is
end entity Decoder_tb;

architecture arch_Decoder_tb of Decoder_tb is

component Decoder_tb is
	generic (
		YFGHJUYTRFCVBH	 : integer;
		U             	 : integer          := 	32;
		N, T          	 : integer;
		GAD           	 : std_logic_vector := 	N-1
	);
	port (
		CLK, rst, yh	 : in  	std_logic;
		Row         	 : in  	std_logic_vector((N-1) downto (N-2));
		Col         	 : out 	std_logic_vector(3 downto 0);
		DecodeOut   	 : out 	std_logic_vector(3 downto 0));
end component;

constant YFGHJUYTRFCVBH	 : integer;
constant U             	 : integer := 	32;
constant N, T            	 : integer;
constant GAD           	 : std_logic_vector := 	N-1;

signal prueba_CLK_intr, prueba_rst_intr, prueba_yh_intr : std_logic;
signal prueba_Row_intr          : std_logic_vector((N-1) downto (N-2));
signal prueba_Col_intr          : std_logic_vector(3 downto 0);
signal prueba_DecodeOut_intr    : std_logic_vector(3 downto 0);

begin

Decoder_inst : Decoder_tb
	generic map (
		YFGHJUYTRFCVBH	 => 	YFGHJUYTRFCVBH,
		U             	 => 	U,
		N             	 => 	N,
		T             	 => 	T,
		GAD           	 => 	GAD,
	)
	port map (
		CLK        => 	prueba_CLK_intr,
		rst        => 	prueba_rst_intr,
		yh         => 	prueba_yh_intr,
		Row        => 	prueba_R_intr,
		Col        => 	prueba_C_intr,
		DecodeOut  => 	prueba_D_intr
	);
end architecture arch_Decoder_tb;