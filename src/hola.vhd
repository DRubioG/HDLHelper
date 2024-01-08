entity hola is
	generic (
		N	 : 	integer := 	32
	);
	port (
		clk    	 : 	in  std_logic;
		rst    	 : 	in  std_logic;
		outport	 : 	out std_logic_vector(3 downto 0));
end entity hola;

