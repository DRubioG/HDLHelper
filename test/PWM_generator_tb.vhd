library IEEE; 
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

entity PWM_generator_tb is
end PWM_generator_tb;

architecture arch_PWM_generator_tb of PWM_generator_tb is
component PWM_generator is
	generic (
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

signal rst : std_logic;
signal clk : std_logic;
signal hab_pwm : std_logic;
signal periodo : std_logic_vector(N-1 downto 0);
signal ciclo_trabajo : std_logic_vector(23 downto 0);
signal pwm_sal : std_logic;
signal final_pwm : std_logic;

begin
DUT : entity work.PWM_generator
	port map(
		rst => rst,
		clk => clk,
		hab_pwm => hab_pwm,
		periodo => periodo,
		ciclo_trabajo => ciclo_trabajo,
		pwm_sal => pwm_sal,
		final_pwm => final_pwm
	);

    rst <= '1', '0' after 50 ns;
    clk <= not(clk) after 10 ns;

end architecture;