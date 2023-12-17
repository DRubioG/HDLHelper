library ieee;
use ieee.std_logic_1164.all;

entity clarke_transformation is
    generic(
        WIDTH_INT : integer := 10;
        WIDTH_DEC : integer := 8
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        en : in std_logic;
        inputA, inputB, inputC : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        start : in std_logic;
        finish : out std_logic;
        alpha, beta : out std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0)
    );
end entity;

architecture arch_clarke_transformation of clarke_transformation is

component matrix_2x3_3x1 is
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
end component;

type clark_coefs is array (0 to 5) of std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
constant clark_coef : clark_coefs := (

);

begin

clacke_tranformation_impl : matrix_2x3_3x1
    generic map(
        WIDTH_INT => 10,
        WIDTH_DEC => 8
    )
    port map(
        clk => clk,
        rst => rst,
        en => en,
        a00 => clark_coef(0),
        a01 => clark_coef(1),
        a02 => clark_coef(2),
        a10 => clark_coef(3),
        a11 => clark_coef(4),
        a12 => clark_coef(5),
        b00 => inputA,
        b10 => inputB
        b20 => inputC,
        start => start,
        finish => finish,
        y0 => alpha,
        y1 => beta
    );


end architecture;