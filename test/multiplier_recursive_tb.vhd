----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/26/2023 07:27:56 PM
-- Design Name: 
-- Module Name: multiplier_recursive_tb - Behavioral
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

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity multiplier_recursive_tb is
--  Port ( );
end multiplier_recursive_tb;

architecture Behavioral of multiplier_recursive_tb is

component multiplier_recursive is
     generic (
        WIDTH : integer := 5
    );
    Port ( 
        clk : in std_logic;
        rst : in std_logic;
        en  : in std_logic;
        start : in std_logic;
        finish : out std_logic;
        a : in std_logic_vector(WIDTH-1 downto 0);
        b : in std_logic_vector(WIDTH-1 downto 0);
        y : out std_logic_vector(2*WIDTH-1 downto 0)
    );
end component;

constant WIDTH : integer := 5;
signal clk : std_logic := '0';
signal rst, en, start, finish : std_logic;
signal a, b : std_logic_vector(WIDTH-1 downto 0);
signal y : std_logic_vector(2*WIDTH-1 downto 0);

begin

DUT : multiplier_recursive 
    generic map (
        WIDTH => WIDTH
    )
    Port map ( 
        clk => clk,
        rst => rst,
        en  => en,
        start => start,
        finish => finish,
        a => a,
        b => b,
        y => y
    );
--    generic map (
--        WIDTH => WIDTH
--    )
--    Port map ( 
--        clk => clk,
--        rst => rst,
--        en  => en,
--        start => start,
--        finish => finish,
--        a => a, 
--        b => b,
--        y => y
--    );

clk <= not clk after 10 ns;
rst <= '1', '0' after 50ns;
a <= "01000";
en <= '1';
b <= "00100";
process begin
    start<='0';
    wait for 100 ns;
    start <= '1';
    wait for 20 ns;
    start <= '0';
    wait;
end process;


end Behavioral;
