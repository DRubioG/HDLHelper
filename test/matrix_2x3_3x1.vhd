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

component matrix_coef_3 is
    generic(
        WIDTH_INT : integer := 10;
        WIDTH_DEC : integer := 8
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        en : in std_logic;
        a0, a1, a2, b0, b1, b2 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        start : in std_logic;
        finish : out std_logic;
        output : out std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0)
    );
end component;

signal finish_r0, finish_r1 : std_logic;

begin
    
    finish <= finish_r0 and finish_r1;

R0 : matrix_coef_3
    generic map (
        WIDTH_INT => WIDTH_INT,
        WIDTH_DEC => WIDTH_DEC
    )
    port map(
        clk => clk,
        rst => rst,
        en => en,
        a0 => a00,
        a1 => a01,
        a2 => a02,
        b0 => b00,
        b1 => a10,
        b2 => b20,
        start => start, 
        finish => finish_r0,
        output => y0
    );

R1 : matrix_coef_3
    generic map (
        WIDTH_INT => WIDTH_INT,
        WIDTH_DEC => WIDTH_DEC
    )
    port map(
        clk => clk,
        rst => rst,
        en => en,
        a0 => a10,
        a1 => a11,
        a2 => a12,
        b0 => b00,
        b1 => a10,
        b2 => b20,
        start => start, 
        finish => finish_r1,
        output => y1
    );


end architecture;