----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/26/2023 12:38:37 PM
-- Design Name: 
-- Module Name: multiplier2_tb - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity multiplier2_tb is
--  Port ( );
end multiplier2_tb;

architecture Behavioral of multiplier2_tb is
    component mult5 is
        port (
            clk, reset : in std_logic;
            a, b : in unsigned(4 downto 0);
            y : out std_logic_vector(9 downto 0)
        );
    end component;
    signal clk : std_logic := '0';
    signal reset : std_logic;
    signal a, b : unsigned(4 downto 0);
    signal y : std_logic_vector(9 downto 0);
begin

DUT : mult5
        port map(
            clk => clk,
            reset => reset,
            a => a,
            b => b,
            y => y
        );

    clk <= not clk after 10ns;
    reset <= '1', '0' after 50ns;
    
    a <= "01111";
    b <= "01111";

end Behavioral;
