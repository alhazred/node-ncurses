 # cat wscript 
def set_options(ctx):
    ctx.tool_options('compiler_cxx')

def configure(ctx):
    ctx.check_tool('compiler_cxx')
    ctx.check_tool('node_addon')
    ctx.link_add_flags()
    ctx.check_cfg(package='',
                path='ncursesw5-config',
                args='--cflags --libs',
                uselib_store='NCURSESW5',
                mandatory=True)

def build(ctx):
    obj = ctx.new_task_gen('cxx', 'shlib', 'node_addon')
    obj.target = 'binding'
    obj.source = 'src/binding.cc'
    obj.cxxflags = ['-O2','-I/usr/local/include/ncursesw'] 
    obj.uselib = ['NCURSESW5']
    obj.lib = ['ncurses++w', 'menuw', 'ncurses', 'panelw'] 
    obj.uselib=['NCURSES5']
