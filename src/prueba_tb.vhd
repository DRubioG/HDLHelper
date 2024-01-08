-----------------------------------------------
-- Created using HDLHelper 0.0
-- Create Date: 2024-01-08 20:00:01.441467
-- Corporation: 
-- Contact: 
-- Version: 
-----------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;
entity prueba_tb is
end entity prueba_tb;

architecture arch_prueba_tb of prueba_tb is

component prueba_tb is
	port (
		port(clk	 : 	in std_logic));
end component;


signal port(clk_i : std_logic);


begin

prueba_inst : prueba_tb
	port map (
		port(clk	 => 	port(clk_i,
	);

	clk <= not(clk) after 5 ns;
	rst <= '0', '1' after 20 ns;

end architecture arch_prueba_tb;