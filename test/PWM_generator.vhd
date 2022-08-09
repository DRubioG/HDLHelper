library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all ;
entity PWM_generator is
    generic(
        N : integer := 32;
        width : integer := 2
    );
    port(
        rst: in std_logic;
        clk: in std_logic;
        hab_pwm: in std_logic;
        periodo: in std_logic_vector(N-1 downto 0);
        ciclo_trabajo: in std_logic_vector(23 downto 0);
        pwm_sal: out std_logic;
        final_pwm: out std_logic);
end PWM_generator;

architecture arch_PWM_generator of PWM_generator is
signal senal_portadora: std_logic_vector(23 downto 0);
--signal periodo_act, ciclo_trabajo_act: std_logic_vector(23 downto 0);
signal final_pwm_int:std_logic;
constant cero: unsigned(23 downto 0):=to_unsigned(0, 24);
begin
    

    process( clk, hab_pwm)
    variable cont:unsigned(23 downto 0);
    begin
    if(rising_edge(clk))then
        if(rst='0')then
            cont:=(others=>'0');
            final_pwm_int<='0';
        elsif(hab_pwm='1')then    
            final_pwm_int<='0';  
            if(cont=cero)then
                final_pwm_int<='1';
                cont:=unsigned(periodo)+1;
            end if;
            cont:=cont-1;   
        elsif (hab_pwm='0') then
            cont:=(others=>'0');
            final_pwm_int<='0';  
        end if;
    end if;
    senal_portadora<=std_logic_vector(cont);
    final_pwm<=final_pwm_int;
    end process;
    
    process(senal_portadora, final_pwm_int)
    variable ciclo_trabajo_act: std_logic_vector(23 downto 0);
    begin
    if (final_pwm_int='1') then
        ciclo_trabajo_act:=ciclo_trabajo;
    end if;
    if(ciclo_trabajo_act=x"000000")then
    	pwm_sal<='0';
    elsif(senal_portadora<=ciclo_trabajo_act)then
        pwm_sal<='1';
    else
        pwm_sal<='0';
    end if;
    
    end process;

end arch_PWM_generator;
