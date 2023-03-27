library IEEE;
use IEEE.std_logic_1164.all;

entity Decoder_tb is
end entity Decoder_tb;
architecture arch_Decoder_tb of Decoder_tb is
	signal clk, rst : std_logic;
	signal row         : std_logic_vector(N-1 downto 0);
	signal col         : std_logic_vector(3 downto 0);
	signal decodeout         : std_logic_vector(3 downto 0);
component Decoder_tb is
	port (
		clk, rst 	 : in  	std_logic;
		row      	 : in  	std_logic_vector(N-1 downto 0);
		col      	 : out 	std_logic_vector(3 downto 0);
		decodeout	 : out 	std_logic_vector(3 downto 0));
end component;

begin
Decoder_tb_inst : Decoder_tb
	port map (
		clk  => clk,
,		rst  => rst,
,		row  => row,		
        col  => col,		
        decodeout => decodeout,	);
end architecture arch_Decoder_tb;