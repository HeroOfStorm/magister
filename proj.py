import seaborn as sns 

class widget_builder:
    
    def __init__(self, data):
        sns_plot_list = ['scatter plot', 'line plot', 'bar plot', 'strip plot', 'swarm plot', 'hist plot', 'joint plot', 'violin plot']
        plot_list = {'scatter plot': sns.scatterplot, 'line plot': sns.lineplot, 'bar plot': sns.barplot, 'strip plot': sns.stripplot, 'swarm plot': sns.swarmplot, 'hist plot': sns.histplot, 'joint plot': sns.jointplot, 'violin plot': sns.violinplot}
        pandas_plot_list = ['scatter', 'line', 'bar', 'barh', 'hist', 'kde', 'density', 'area', 'pie', 'hexbin']
        self.df_in_widget = data

        if data.shape > (2,2):
        
            if (self.num_cols ::= self.check_for_numericals(data)):          
                print(data.columns)
                print('numeric', self.num_cols)

            if (self.cat_cols ::= self.check_for_categorycals(data)): 
                print('Category', self.cat_cols, '\n', self.cat_cols[0], self.num_cols[0])
                try:
                    display(data.plot(x=self.cat_cols[0], y=self.num_cols[0], kind='barh'))
                except:
                    display(data.plot(ylabel=self.cat_cols[0], kind='barh'))
                    
                    
    def adaptable_widget(self, numerical_columns, categorycal_columns):
        num_rows = len(self.df_in_widget)
        display(self.df_in_widget)

        # Create some plots
        fig, axs = plt.subplots(ncols=1, figsize=(12, 6))
        print(numerical_columns)
        sns.barplot(data=self.df_in_widget,  y=numerical_columns, x=categorycal_columns)
        plt.show()

        # Display the summary statistics
        print(f"Number of rows: {num_rows}")
        
    def check_for_numericals(self, df_in):
    #     any_numerical = False
        numerical_columns = []
        for column_name, coluns_data in df_in.iteritems():
            if pd.api.types.is_numeric_dtype(coluns_data):
    #             any_numerical = True
                numerical_columns.append(column_name)

        return numerical_columns

    def check_for_categorycals(self, df_in):
    #     any_categorycal = False
        categorycal_columns = []
        di_cate_col = {}
        for column_name, coluns_data in df_in.iteritems():
            if len(set(coluns_data)) > 1 and df_in[column_name].value_counts().mean() > 1 and column_name not in self.num_cols:
    #             any_categorycal = True
                di_cate_col[df_in[column_name].nunique()] = column_name
                categorycal_columns.append(column_name)

        print(di_cate_col)
        return categorycal_columns