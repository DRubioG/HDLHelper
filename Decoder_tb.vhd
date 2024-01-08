-----------------------------------------------
-- User: 
-- Corporation: 
-- Contact: 
-- Version: 
-----------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;
entity Decoder_tb is
end entity Decoder_tb;

architecture arch_Decoder_tb of Decoder_tb is

component Decoder_tb is
	generic (
		YFG6YUGIUKJ	 : 	integer
		U          	 : 	integer          := 	32;
		N          	 : 	integer;
		T          	 : 	integer;
		GAD        	 : 	std_logic_vector := 	N-1;
	);
	port (
		clk                  	 : 	in  std_logic);
		rst                  	 : 	in  std_logic);
		yhmm                 	 : 	in  std_logic);
		Rowerererrererererere	 : 	in  std_logic_vector((N-1) downto (N-2));
		Col                  	 : 	out std_logic_vector(3 downto 0);
		DecodeOut            	 : 	out std_logic_vector(3 downto 0);
end component;

constant YFG6YUGIUKJ : integer;
constant U           : integer	 := 32;
constant N           : integer;
constant T           : integer;
constant GAD         : std_logic_vector	 := N-1;

signal clk                   : std_logic;
signal rst                   : std_logic;
signal yhmm                  : std_logic;
signal Rowerererrererererere : std_logic_vector((N-1) downto (N-2));
signal Col                   : std_logic_vector(3 downto 0);
signal DecodeOut             : std_logic_vector(3 downto 0);


begin

Decoder_inst : Decoder_tb
	generic map (
		YFG6YUGIUKJ
		U,
		N,
		T,
		GAD,
	)
	port map (
		clk,
		rst,
		yhmm,
		Rowerererrererererere
		Col,
		DecodeOut,
	);



end architecture arch_Decoder_tb;