from Backend.HDL import *
from Backend.VHDL_regen import *
import json, datetime, os


class Testbench_vhdl():
    """ 
    This method creates the Testbench files.
    For this operation it uses the classes HDL, that read the file that
    wants to create the testbench and return the list with all the neccesary 
    information. And the VHDL_regen class has all the methods for create VHDL testbench file.
    """
    
    def __init__(self, file_input, file_output):
        self.file_input = file_input
        self.name = self.file_input[:-4]
        self.file_output = file_output
        self.regen = VHDL_regen()
        self.load_config()
        self.testbench()

    def load_config(self):
        """
        This method reads config file and creates properties that is going to use
        by other methods.
        """

        try:
            file = open("./config/configuration.json", 'r')
            data = json.load(file)      # get the configuration parameters
            self.version = data["version"]

            self.tool_comments = data["preferences"][0]["tool_comments"]
            self.user = data["preferences"][0]["user"]
            self.corporation = data["preferences"][0]["corporation"]
            self.contact = data["preferences"][0]["contact"]
            self.user_version = data["preferences"][0]["user_version"]
            self.tool_version_fl = data["preferences"][0]["tool_version"]
            self.date_fl = data["preferences"][0]["date"]

            self.vhdl_version = data["Testbench_generator"][0]["version"]
            self.tab_spaces = data["Testbench_generator"][0]["tab_spaces"]
            self.spaces = data["Testbench_generator"][0]["spaces"]
            self.ftext = data["Testbench_generator"][0]["ftext"]
            self.etext = data["Testbench_generator"][0]["etext"]
            self.uppercase_generics = data["Testbench_generator"][0]["uppercase_generics"]
            self.uppercase_ports = data["Testbench_generator"][0]["uppercase_ports"]
            self.default_config = data["Testbench_generator"][0]["default_config"]
            self.comments_load = data["Testbench_generator"][0]["comments"]
        except:
            self.version = "unkown"

            self.tool_comments = "True"
            self.user = ""
            self.corporation = ""
            self.contact = ""
            self.user_version = ""
            self.tool_version_fl = "False"
            self.date_fl = "False"

            self.vhdl_version = "87"
            self.tab_spaces = "tab"
            self.spaces = "4"
            self.ftext = ""
            self.etext = ""
            self.uppercase_generics = "True"
            self.uppercase_ports = "False"
            self.comments_load = "False"


    def testbench(self):
        """
        This method generates the VHDL testbench.
        This method has the structure of VHDL testbench files.
        First, it gets the list of the VHDL file
        Second, it generates the testbench file and completes with the list
        Thrid, it closes the file
        """

        self.hdl = HDL(self.file_input) # creates an HDL object
        # get ports, generics, comments and the entity(only for a direct copy option) from the file
        self.ports, self.generics, self.comments, self.entity = self.hdl.init()

        self.open_file(self.file_output)    # generates the testbench file
        name = self.file_output[:-4]        # extract the name of the file
        _, name = os.path.split(name)
        output = self.write_tool_comments() # insert the tool comments  
        output += self.write_libraries()    # write the libraries of the testbench file
        output += self.write_entity(name)   # write the entity part
        # write the architecture part
        output += self.write_architecture(name, self.generics, 
                                          self.ports, self.comments, self.entity, self.default_config, copy_flag=True)
        self.close_file(output)     # close the file


    def open_file(self, output_file):
        """
        This method creates the testbench file with the name of the testbench
        """
        self.file = open(output_file, 'w')


    def write_tool_comments(self):
        """
        This method writes the main comments of the tool
        Return:
            - string with the initial comments
        """
        if self.tool_comments == "True":
            wr = "-----------------------------------------------\n"
            if self.tool_version_fl == "True":
                wr += "-- Created using HDLHelper "+ self.version + "\n"
            if self.user != "":
                wr += "-- User: " + self.user + "\n"
            if self.date_fl == "True":
                wr += "-- Create Date: " + str(datetime.datetime.now()) + "\n"
            if self.corporation != "":
                wr += "-- Corporation: " + self.corporation + "\n"
            if self.contact != "":
                wr += "-- Contact: " + self.contact + "\n"
            if self.user_version != "":
                wr += "-- Version: " + self.user_version + "\n"
            wr += "-----------------------------------------------\n\n"
            return wr
        else:
            return ""


    def write_libraries(self):
        """
        This method adds the libraries for the testbench
        Return:
            - string with libraries part written
        """
        libraries = []
        for type in self.ports:
            if type == "unsigned":
                libraries.append("numeric_std")
        output = self.regen.libraries(self.file, libraries)
        return output


    def write_entity(self, name):
        """
        This method writes the entity part of the testbench.
        Because testbench entity is empty, entity method only has a name as parameter.
        Return:
            - string with entity part written
        """
        # components = [self.ports, self.generics, self.comments]

        output = self.regen.entity(name)
        return output


    def write_architecture(self, name, generics, ports, comments, entity, default_config, copy_flag):
        """
        This method generates the architecture part with the specific option.
        Input:
            - name: name of the testbench file
            - generics: list of generics
            - ports: list of ports
            - comments: list of comments
            - entity: list with the entity(only for a direct copy option)
            - default config: 
            - copy_flag: 
        Return:
            - string with all the architecture part written
        """
        output = self.regen.architecture(name, generics=generics, ports=ports, comments=comments, entity=entity, vhdl_version=self.vhdl_version, component=True, copy=copy_flag,
                                         uppercase_gen_cfg=self.uppercase_generics, uppercase_port_cfg=self.uppercase_ports, tab_space_cfg=self.tab_spaces, 
                                         etext=self.etext, ftext=self.ftext, default_config=self.default_config)

        return output


    def close_file(self, output):
        """
        This method writes all the lines of the testbench and close it.
        """
        self.file.write(output)
        self.file.close()
