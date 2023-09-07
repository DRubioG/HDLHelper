library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

entity RX is
generic(
    tiempo: integer:=1000;
    N: integer:=32;
    rst_en: std_logic :='1'
);
port (
    clk: in std_logic;
    rst: in std_logic;
    rx_in: in std_logic;
    data_in: out std_logic_vector(N-1 downto 0);
    data_rx_ok : out std_logic
    );
end RX;
