library ieee;
use ieee.std_logic_1164.all;

entity matrix_2x3_3x1 is
    generic(
        WIDTH_INT : integer := 10;
        WIDTH_DEC : integer := 8
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        en : in std_logic;
        a00, a01, a02, a10, a11, a12 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        b00, b10, b20 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        start : in std_logic;
        finish : out std_logic;
        y0, y1 : out std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0)
    );
end entity;

architecture arch_matrix_2x3_3x1 of matrix_2x3_3x1 is