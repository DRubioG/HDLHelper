library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity hola is


entity hola;

architecture arch_hola of hola is

component PWM_generator 
generic(
	N : integer := 32;
	width : integer := 2
	);
port (
	rst : in std_logic;
	clk : in std_logic;
	hab_pwm : in std_logic;
	periodo : in std_logic_vector(N-1 downto 0);
	ciclo_trabajo : in std_logic_vector(23 downto 0);
	pwm_sal : out std_logic;
	final_pwm : out std_logic
	);
end component;


begin
PWM_generator_impl : entity work.PWM_generator
	generic map(
		N => N_top,
		width => width_top,
	)
	port map(
		rst => rst_top,
		clk => clk_top,
		hab_pwm => hab_pwm_top,
		periodo => periodo_top,
		ciclo_trabajo => ciclo_trabajo_top,
		pwm_sal => pwm_sal_top,
		final_pwm => final_pwm_top
	);

end arch_hola