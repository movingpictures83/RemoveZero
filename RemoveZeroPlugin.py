import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class RemoveZeroPlugin:
   def input(self, filename):
      filestuff = open(filename, 'r')
      firstline = filestuff.readline().strip() # Read first line
      self.taxa = firstline.split(',')
      #self.taxa.remove(self.taxa[0])  # Remove placeholder

      # Possibly remove quotes
      #for i in range(len(self.taxa)):
      #   if self.taxa[i][0] == '\"':
      #      self.taxa[i] = self.taxa[i][1:len(self.taxa[i])-1]

      self.lines = []
      for line in filestuff:
         self.lines.append(line.strip())

      self.sums = dict()
      for taxon in self.taxa:
         self.sums[taxon] = 0

   def run(self):
      for line in self.lines:
         elements = line.split(',')
         for i in range(1, len(elements)): # Don't count the sample
            if (not is_number(elements[i])):
               self.sums[self.taxa[i]] += 1
            else:
               self.sums[self.taxa[i]] += float(elements[i])
      
      for i in range(1, len(self.taxa)):
         if (self.sums[self.taxa[i]] == 0):
            self.taxa[i] = "ABSENT"  # flag

   def output(self,filename):
      outstuff = open(filename, 'w')
      outstuff.write(self.taxa[0])
      for i in range(1, len(self.taxa)):
         if (self.taxa[i] != "ABSENT"):
            outstuff.write(","+self.taxa[i])
         if (i == len(self.taxa)-1):
            outstuff.write("\n")

      for line in self.lines:
         elements = line.split(',')
         outstuff.write(elements[0])
         for i in range(1, len(elements)):
            if (self.taxa[i] != "ABSENT"):
               outstuff.write(","+elements[i])
            if (i == len(self.taxa)-1):
               outstuff.write("\n")       

