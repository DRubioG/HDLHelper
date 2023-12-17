library ieee;
use ieee.std_logic_1164.all;

entity matrix_3x3_3x3 is
    generic(
        WIDTH_INT : integer := 10;
        WIDTH_DEC : integer := 8
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        en : in std_logic;
        a00, a01, a02, a10, a11, a12, a20, a21, a22 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        b00, b01, b02, b10, b11, b12, b20, b21, b22 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        start : in std_logic;
        finish : out std_logic;
        y00, y01, y02, y10, y11, y12, y20, y21, y22 : out std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0)
    );
end entity;

architecture arch_matrix_2_3 of matrix_2_3 is

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


signal finish_r00, finish_r01, finish_r02, finish_r10, finish_r11, finish_r12, finish_r20, finish_r21, finish_r22 : std_logic;

begin

    finish <= finish_r00 and finish_r01 and finish_r02 and finish_r10 and finish_r11 and finish_r12 and finish_r20 and finish_r21 and finish_r22;

R00 : matrix_coef_3
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
        finish => finish_r00,
        output => y00
    );

R01 : matrix_coef_3
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
        finish => finish_r01,
        output => y01
    );

R02 : matrix_coef_3
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
        finish => finish_r02,
        output => y02
    );

R10 : matrix_coef_3
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
        finish => finish_r10,
        output => y10
    );

R11 : matrix_coef_3
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
        finish => finish_r11,
        output => y11
    );

R12 : matrix_coef_3
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
        finish => finish_r12,
        output => y12
    );

R20 : matrix_coef_3
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
        finish => finish_r20,
        output => y20
    );

R21 : matrix_coef_3
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
        finish => finish_r21,
        output => y21
    );

R22 : matrix_coef_3
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
        finish => finish_r22,
        output => y22
    );




end architecture;