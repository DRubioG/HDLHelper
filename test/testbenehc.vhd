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

entity testbenehc is
--  Port ( );
end testbenehc;

architecture Behavioral of testbenehc is

component multplier_recursive is
     generic (
        WIDTH : integer 
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

constant WIDTH : integer := 31;
signal clk : std_logic := '0';
signal rst, en, start, finish : std_logic;
signal a, b : std_logic_vector(WIDTH-1 downto 0);
signal y : std_logic_vector(2*WIDTH-1 downto 0);

begin

clk <= not clk after 10 ns;
rst <= '1', '0' after 50ns;
a <= (1=>'1', 4=>'1', 12=>'1', 23=>'1', 30=>'1', others=>'0');
en <= '1';
b <= (1=>'1', 4=>'1', 12=>'1', 23=>'1', 30=>'1', others=>'0');
process begin
    start<='0';
    wait for 100 ns;
    start <= '1';
    wait for 20 ns;
    start <= '0';
    wait;
end process;

DUT : multplier_recursive 
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

end Behavioral;
